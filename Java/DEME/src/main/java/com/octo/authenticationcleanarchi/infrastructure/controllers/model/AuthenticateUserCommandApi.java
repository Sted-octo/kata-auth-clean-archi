package com.octo.authenticationcleanarchi.infrastructure.controllers.model;

import com.octo.authenticationcleanarchi.usecases.model.AuthenticateUserCommand;
import jakarta.validation.constraints.NotNull;

public record AuthenticateUserCommandApi(@NotNull String name, @NotNull String password) {
    public AuthenticateUserCommand toCommand() {
        return new AuthenticateUserCommand(name, password);
    }
}
