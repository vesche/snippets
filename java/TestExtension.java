/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package testextension;

import com.smartfoxserver.v2.extensions.SFSExtension;
import com.smartfoxserver.v2.core.SFSEventType;

public class TestExtension extends SFSExtension {
    
    @Override
    public void init()
    {
       trace("My CustomLogin extension starts!"); 

       // Register for login event
       addEventHandler(SFSEventType.USER_LOGIN, LoginEventHandler.class);
       addRequestHandler("SumNumbers", SumNumbersHandler.class);
    }
}
