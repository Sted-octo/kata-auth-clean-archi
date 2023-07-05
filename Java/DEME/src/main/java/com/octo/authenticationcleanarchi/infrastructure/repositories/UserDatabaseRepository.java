package com.octo.authenticationcleanarchi.infrastructure.repositories;

import com.octo.authenticationcleanarchi.usecases.ports.UserRepository;
import org.springframework.stereotype.Repository;

@Repository
public class UserDatabaseRepository implements UserRepository {

    @Override
    public boolean existsWithNameAndPassword(String name, String password) {
        if (name.compareTo("dexter") == 0 && password.compareTo("killer") == 0)
            return true;
        return false;
    }
}
