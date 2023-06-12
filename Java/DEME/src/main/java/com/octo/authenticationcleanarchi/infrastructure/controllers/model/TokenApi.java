package com.octo.authenticationcleanarchi.infrastructure.controllers.model;

import com.octo.authenticationcleanarchi.usecases.model.Token;

public record TokenApi(String value) {
    public TokenApi(Token token) {
        this(token.value());
    }
}

