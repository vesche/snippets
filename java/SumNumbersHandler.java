/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testextension;

import com.smartfoxserver.v2.entities.User;
import com.smartfoxserver.v2.entities.data.ISFSObject;
import com.smartfoxserver.v2.entities.data.SFSObject;
import com.smartfoxserver.v2.extensions.BaseClientRequestHandler;

public class SumNumbersHandler extends BaseClientRequestHandler {
    @Override
    public void handleClientRequest(User user, ISFSObject objIn)
    {
        int numA = objIn.getInt("NumA");
        int numB = objIn.getInt("NumB");
        
        ISFSObject objOut = new SFSObject();
        objOut.putInt("NumC", numA + numB);
        
        send("SumNumbers", objOut, user);
    }
}
