package com.octo.authenticationcleanarchi.infrastructure.controllers;

import com.octo.authenticationcleanarchi.infrastructure.controllers.model.UnauthorizedApiException;
import com.octo.authenticationcleanarchi.infrastructure.controllers.model.TokenApi;
import com.octo.authenticationcleanarchi.infrastructure.controllers.model.AuthenticateUserCommandApi;
import com.octo.authenticationcleanarchi.usecases.AuthenticateUser;
import com.octo.authenticationcleanarchi.usecases.model.AuthenticateUserCommand;
import com.octo.authenticationcleanarchi.usecases.model.Token;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/auth")
public class AuthenticationController {

    private final AuthenticateUser authenticateUser;

    @Autowired
    public AuthenticationController(AuthenticateUser authenticateUser) {
        this.authenticateUser = authenticateUser;
    }

    @PostMapping
    public TokenApi authenticate(@Valid @RequestBody AuthenticateUserCommandApi authenticateUserCommandApi) throws UnauthorizedApiException {
        AuthenticateUserCommand authenticateUserCommand = authenticateUserCommandApi.toCommand();

        try {
            Token token = authenticateUser.execute(authenticateUserCommand);
            return new TokenApi(token);

        } catch (Exception e) {
            throw new UnauthorizedApiException();
        }
    }

}
