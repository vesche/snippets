using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Sfs2X;
using Sfs2X.Core;
using Sfs2X.Requests;
using Sfs2X.Entities;
using Sfs2X.Entities.Data;

//
// this is an old file that is not being used, i'm just keeping it here for reference
//

public class Connect : MonoBehaviour {
    // init vars
    public string serverIP = "127.0.0.1";
    public int serverPort = 9933;
    public string zoneName = "BasicExamples";
    public string userName = "jackson";
    public string password = "isthebest";
    public string roomName = "The Lobby";

    SmartFox sfs;

    // Use this for initialization
    void Start() {
        sfs = new SmartFox();
        sfs.ThreadSafeMode = true;

        sfs.AddEventListener(SFSEvent.CONNECTION, OnConnection);
        sfs.AddEventListener(SFSEvent.LOGIN, OnLogin);
        sfs.AddEventListener(SFSEvent.LOGIN_ERROR, OnLoginError);


        // sfs.AddEventListener(SFSEvent.EXTENSION_RESPONSE, OnExtensionResponse);

        //
        // sfs.AddEventListener(SFSEvent.ROOM_JOIN, OnJoinRoom);
        // sfs.AddEventListener(SFSEvent.ROOM_JOIN_ERROR, OnJoinRoom);
        // sfs.AddEventListener(SFSEvent.PUBLIC_MESSAGE, OnPublicMessage);
        //

        sfs.Connect(serverIP, serverPort);
    }

    // Update is called once per frame
    void Update() {
        sfs.ProcessEvents();
    }

    private void OnApplicationQuit()
    {
        if (sfs.IsConnected)
        {
            sfs.Disconnect();
        }
    }

    void OnConnection(BaseEvent e)
    {
        if ((bool)e.Params["success"])
        {
            Debug.Log("Successfully connected!");

            sfs.Send(new LoginRequest(userName, password, zoneName));
        }
        else
        {
            Debug.Log("Connection failed!");
        }
    }

    void OnLogin(BaseEvent e)
    {
        Debug.Log("Logged In: " + e.Params["user"]);

        // testing TestExtension SumNumbersHandler
        //
        // ISFSObject objOut = new SFSObject();
        // objOut.PutInt("NumA", 12);
        // objOut.PutInt("NumB", 24);
        // sfs.Send(new ExtensionRequest("SumNumbers", objOut));

        // testing joining rooms
        //
        // sfs.Send(new JoinRoomRequest(roomName));

    }

    void OnLoginError(BaseEvent e)
    {
        Debug.Log("Login Error: " + e.Params["errorCode"] + e.Params["errorMessage"]);
    }



    /*


    void OnExtensionResponse(BaseEvent e)
    {
        string cmd = (string)e.Params["cmd"];
        ISFSObject objIn = (SFSObject)e.Params["params"];
        if (cmd == "SumNumbers")
        {
            Debug.Log("Sum: " + objIn.GetInt("NumC"));
        }
    }

    void OnJoinRoom(BaseEvent e)
    {
        Debug.Log("Joined Room: " + e.Params["room"]);

        sfs.Send(new PublicMessageRequest("Hello, world!"));
    }

    void OnJoinRoomError(BaseEvent e)
    {
        Debug.Log("Joined Room Error: " + e.Params["errorCode"] + e.Params["errorMessage"]);
    }

    void OnPublicMessage(BaseEvent e)
    {
        Room room = (Room)e.Params["room"];
        User sender = (User)e.Params["sender"];
        Debug.Log("[" + room.Name + "]" + sender.Name + ": " + e.Params["message"]);
    }


     */


}
