using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using UnityEngine.EventSystems;
using Sfs2X;
using Sfs2X.Core;
using Sfs2X.Requests;

public class Login : MonoBehaviour {
    // globals
    public string serverIP = "54.165.34.161";
    public int serverPort = 9933;
    public string zoneName = "BasicExamples";

    // ui
    public InputField usernameInput;
    public InputField passwordInput;
    public Button loginButton;
    public Text errorText;

    // priv
    private SmartFox sfs;

    // Use this for initialization
    void Start()
    {
        usernameInput.text = "";
        passwordInput.text = "";
        errorText.text = "";
    }

    // Update is called once per frame
    void Update()
    {
        if (sfs != null)
            sfs.ProcessEvents();

        // tab field hack
        if (Input.GetKeyDown(KeyCode.Tab))
        {
            if (usernameInput.isFocused)
            {
                EventSystem.current.SetSelectedGameObject(passwordInput.gameObject, null);
                passwordInput.OnPointerClick(new PointerEventData(EventSystem.current));
            }
            if (passwordInput.isFocused)
            {
                EventSystem.current.SetSelectedGameObject(usernameInput.gameObject, null);
                usernameInput.OnPointerClick(new PointerEventData(EventSystem.current));
            }
        }

        // press enter for login
        if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.KeypadEnter))
            OnLoginButtonClick();
    }

    // public interface method for ui
    public void OnLoginButtonClick()
    {
        sfs = new SmartFox();
        sfs.ThreadSafeMode = true;

        sfs.AddEventListener(SFSEvent.CONNECTION, OnConnection);
        sfs.AddEventListener(SFSEvent.LOGIN, OnLogin);
        sfs.AddEventListener(SFSEvent.LOGIN_ERROR, OnLoginError);
        sfs.AddEventListener(SFSEvent.ROOM_JOIN, OnRoomJoin);
        sfs.AddEventListener(SFSEvent.ROOM_JOIN_ERROR, OnRoomJoinError);

        sfs.Connect(serverIP, serverPort);
    }

    void OnConnection(BaseEvent e)
    {
        if ((bool)e.Params["success"])
        {
            Debug.Log("Successfully connected to server!");

            // Save reference to SmartFox instance to be used in other scenes!
            SmartFoxConnection.Connection = sfs;

            sfs.Send(new LoginRequest(usernameInput.text, passwordInput.text, zoneName));
        }
        else
        {
            errorText.text = "Could not connect to the server!";
        }
    }

    void OnLogin(BaseEvent e)
    {
        errorText.text = "Logged In: " + e.Params["user"];

        sfs.Send(new JoinRoomRequest("The Lobby"));
    }

    void OnLoginError(BaseEvent e)
    {
        errorText.text = "Login Error: " + e.Params["errorMessage"];
    }

    void OnRoomJoin(BaseEvent e)
    {
        // remove sfs2x listeners and re-enable interface
        sfs.RemoveAllEventListeners();

        // load into game
        SceneManager.LoadScene("main");
    }

    void OnRoomJoinError(BaseEvent e)
    {
        errorText.text = "Room join failed: " + e.Params["errorMessage"];
    }

    private void OnApplicationQuit()
    {
        sfs.Disconnect();
    }
}
