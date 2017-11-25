/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package loginextension;

import com.smartfoxserver.v2.extensions.SFSExtension;
import com.smartfoxserver.v2.components.login.LoginAssistantComponent;

public class LoginExtension extends SFSExtension
{
    private LoginAssistantComponent lac;

    @Override
    public void init()
    {
        lac = new LoginAssistantComponent(this);

        // Configure the component
        lac.getConfig().loginTable = "users";
        lac.getConfig().userNameField = "username";
        lac.getConfig().passwordField = "password";
    }

    @Override
    public void destroy()
    {
        super.destroy();
        // lac.destroy();
    }
}
