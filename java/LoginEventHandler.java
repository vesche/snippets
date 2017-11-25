/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testextension;

import com.smartfoxserver.v2.extensions.BaseServerEventHandler;
import com.smartfoxserver.v2.core.ISFSEvent;
import com.smartfoxserver.v2.exceptions.SFSException;
import com.smartfoxserver.v2.core.SFSEventParam;
import com.smartfoxserver.v2.exceptions.SFSErrorData;
import com.smartfoxserver.v2.exceptions.SFSErrorCode;
import com.smartfoxserver.v2.exceptions.SFSLoginException;

public class LoginEventHandler extends BaseServerEventHandler
{
   @Override
   public void handleServerEvent(ISFSEvent event) throws SFSException
   {
      String name = (String) event.getParameter(SFSEventParam.LOGIN_NAME); 
 
      if (name.equals("Gonzo") || name.equals("Kermit"))
      {
 
        // Create the error code to send to the client
        SFSErrorData errData = new SFSErrorData(SFSErrorCode.LOGIN_BAD_USERNAME);
        errData.addParameter(name);
 
        // Fire a Login exception
        throw new SFSLoginException("Gonzo and Kermit are not allowed in this Zone!", errData);
      }
   }
}
