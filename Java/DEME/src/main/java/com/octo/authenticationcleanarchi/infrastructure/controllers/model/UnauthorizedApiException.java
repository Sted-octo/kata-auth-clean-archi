package com.octo.authenticationcleanarchi.infrastructure.controllers.model;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.UNAUTHORIZED)
public class UnauthorizedApiException extends Exception {
}
