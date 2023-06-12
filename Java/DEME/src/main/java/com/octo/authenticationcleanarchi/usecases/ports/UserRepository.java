package com.octo.authenticationcleanarchi.usecases.ports;

public interface UserRepository {
    boolean existsWithNameAndPassword(String name, String password);
}
