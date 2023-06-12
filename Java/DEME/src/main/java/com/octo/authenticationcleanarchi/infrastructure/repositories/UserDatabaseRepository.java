package com.octo.authenticationcleanarchi.infrastructure.repositories;

import com.octo.authenticationcleanarchi.usecases.ports.UserRepository;
import org.springframework.stereotype.Repository;

@Repository
public class UserDatabaseRepository implements UserRepository {

    @Override
    public boolean existsWithNameAndPassword(String name, String password) {
        return false;
    }
}
