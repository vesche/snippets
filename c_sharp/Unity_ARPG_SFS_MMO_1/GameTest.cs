using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;
using System.Collections;
using System.Collections.Generic;
using Sfs2X;
using Sfs2X.Core;
using Sfs2X.Entities;
using Sfs2X.Entities.Data;
using Sfs2X.Entities.Variables;
using Sfs2X.Requests;


public class GameTest : MonoBehaviour {

    // ui
    public Button logoutButton;
    public InputField chatInput;
    public Text chatText;
    public ScrollRect chatScrollView;

    // game stuff
    public Text playerName;

    // priv
    private SmartFox sfs;

    // for spawning player & movement
    public GameObject playerObject;
    private GameObject localPlayer;
    private PlayerController localPlayerController;
    private Dictionary<SFSUser, GameObject> remotePlayers = new Dictionary<SFSUser, GameObject>();

    // get smartfox goin again
    private void Awake()
    {
        // need to look up what this even does
        Application.runInBackground = true;

        if (SmartFoxConnection.IsInitialized)
        {
            sfs = SmartFoxConnection.Connection;
        }
        else
        {
            SceneManager.LoadScene("main");
            return;
        }

        sfs.ThreadSafeMode = true;

        sfs.AddEventListener(SFSEvent.OBJECT_MESSAGE, OnObjectMessage);
        sfs.AddEventListener(SFSEvent.CONNECTION_LOST, OnConnectionLost);
        sfs.AddEventListener(SFSEvent.USER_VARIABLES_UPDATE, OnUserVariableUpdate);
        sfs.AddEventListener(SFSEvent.USER_ENTER_ROOM, OnUserEnterRoom);
        sfs.AddEventListener(SFSEvent.USER_EXIT_ROOM, OnUserExitRoom);
        sfs.AddEventListener(SFSEvent.PUBLIC_MESSAGE, OnPublicMessage);

        // spawn the player
        SpawnLocalPlayer();

        // update ui here in the future for color stuff
    }

    // Use this for initialization
    void Start () {
        chatInput.text = "";
        chatText.text = "";
        playerName.text = "test";
	}
	
	// Update is called once per frame
	void Update () {
        if (sfs != null)
        {
            sfs.ProcessEvents();

            if (localPlayer != null && localPlayerController != null && localPlayerController.MovementDirty)
            {
                List<UserVariable> userVariables = new List<UserVariable>();
                userVariables.Add(new SFSUserVariable("x", (double)localPlayer.transform.position.x));
                userVariables.Add(new SFSUserVariable("y", (double)localPlayer.transform.position.y));
                sfs.Send(new SetUserVariablesRequest(userVariables));
                localPlayerController.MovementDirty = false;
            }
        }

        if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter))
            OnSendMessageButtonClick();
    }

    // built in NET app quit lets get rid of player
    private void OnApplicationQuit()
    {
        RemoveLocalPlayer();
    }

    private void RemoveLocalPlayer()
    {
        // Someone dropped off the grid. Lets remove em
        SFSObject obj = new SFSObject();
        obj.PutUtfString("cmd", "rm");
        sfs.Send(new ObjectMessageRequest(obj, sfs.LastJoinedRoom));
    }

    // public interaction for send button
    public void OnSendMessageButtonClick()
    {
        if (chatInput.text != "")
        {
            sfs.Send(new Sfs2X.Requests.PublicMessageRequest(chatInput.text));

            // clear out chat input after sending
            chatInput.text = "";
        }
    }

    // all my movement stuff...

    private void SpawnLocalPlayer()
    {
        Vector3 pos;

        // that's kinda like the middle of the screen
        pos = new Vector3(0, 0);

        localPlayer = GameObject.Instantiate(playerObject) as GameObject;
        localPlayer.transform.position = pos;

        // add controller
        localPlayer.AddComponent<PlayerController>();
        localPlayerController = localPlayer.GetComponent<PlayerController>();

        // fix camera
        Camera.main.transform.parent = localPlayer.transform;

        // set name above head **** This isn't a thing yet
        // localPlayer.GetComponentInChildren<Text>().text = sfs.MySelf.Name;
        // this is temporary...
        playerName.text = "Logged in as: " + sfs.MySelf.Name;
        Debug.Log("Logged in as: " + sfs.MySelf.Name);

        // send color here in the future?
    }

    private void SpawnRemotePlayer(SFSUser user, Vector3 pos)
    {
        // see if already exists so we can destroy first
        // ???
        if (remotePlayers.ContainsKey(user) && remotePlayers[user] != null)
        {
            Destroy(remotePlayers[user]);
            remotePlayers.Remove(user);
        }

        // Lets spawn our remote player model
        GameObject remotePlayer = GameObject.Instantiate(playerObject) as GameObject;
        remotePlayer.AddComponent<SimpleRemoteInterpolation>();
        remotePlayer.GetComponent<SimpleRemoteInterpolation>().SetTransform(pos, false);

        // Lets track the dude
        remotePlayers.Add(user, remotePlayer);

    }

    private void OnObjectMessage(BaseEvent e)
    {
        // The only messages being sent around are remove messages from users that are leaving the game
        ISFSObject dataObj = (SFSObject)e.Params["message"];
        SFSUser sender = (SFSUser)e.Params["sender"];

        if (dataObj.ContainsKey("cmd"))
        {
            switch (dataObj.GetUtfString("cmd"))
            {
                case "rm":
                    Debug.Log("Removing player unit " + sender.Id);
                    RemoveRemotePlayer(sender);
                    break;
            }
        }

    }

    // LOTSA GAME LOGIC
    private void OnUserVariableUpdate(BaseEvent e)
    {
        List<string> changedVars = (List<string>)e.Params["changedVars"];

        SFSUser user = (SFSUser)e.Params["user"];
        if (user == sfs.MySelf) return;

        if (!remotePlayers.ContainsKey(user))
        {
            // New client just started transmitting - lets create remote player
            Vector3 pos = new Vector3(0, 0);
            if (user.ContainsVariable("x") && user.ContainsVariable("y"))
            {
                pos.x = (float)user.GetVariable("x").GetDoubleValue();
                pos.y = (float)user.GetVariable("y").GetDoubleValue();
            }
            
            SpawnRemotePlayer(user, pos);
        }

        // Check if the remote user changed position
        if (changedVars.Contains("x") && changedVars.Contains("y"))
        {
            // Move the character to a new position... (holy shit lol)
            remotePlayers[user].GetComponent<SimpleRemoteInterpolation>().SetTransform(
                new Vector3((float)user.GetVariable("x").GetDoubleValue(), (float)user.GetVariable("y").GetDoubleValue()), true);
        }
    }

    private void OnUserEnterRoom(BaseEvent e)
    {
        // so if you're standing still everyone can get your player loc (cause of movement dirty)
        if (localPlayer != null)
        {
            List<UserVariable> userVariables = new List<UserVariable>();
            userVariables.Add(new SFSUserVariable("x", (double)localPlayer.transform.position.x));
            userVariables.Add(new SFSUserVariable("y", (double)localPlayer.transform.position.y));
            sfs.Send(new SetUserVariablesRequest(userVariables));
        }
    }

    private void OnUserExitRoom(BaseEvent e)
    {
        SFSUser user = (SFSUser)e.Params["user"];
        RemoveRemotePlayer(user);
    }

    private void RemoveRemotePlayer(SFSUser user)
    {
        if (user == sfs.MySelf) return;

        if (remotePlayers.ContainsKey(user))
        {
            Destroy(remotePlayers[user]);
            remotePlayers.Remove(user);
        }
    }

    // chat and other shit...

    private void OnPublicMessage(BaseEvent e)
    {
        User sender = (User)e.Params["sender"];
        string message = (string)e.Params["message"];

        chatText.text += " " + sender.Name + ": " + message + "\n";

        // scroll view to bottom
        chatScrollView.verticalNormalizedPosition = 0;

    }

    private void OnConnectionLost(BaseEvent e)
    {
        sfs.RemoveAllEventListeners();
        sfs.Disconnect(); // might not need this?
        SceneManager.LoadScene("main");
    }

    // public interface for logoutButton
    public void OnLogoutButtonClick()
    {
        sfs.Disconnect();

        SceneManager.LoadScene("main");
    }

    // print message on chatbox
    //public void printMessage(string message)
    //{
    //    chatText.text += sfs.MySelf.Name + ": " + message + "\n";
    //
    //    Canvas.ForceUpdateCanvases();
    //}
}
