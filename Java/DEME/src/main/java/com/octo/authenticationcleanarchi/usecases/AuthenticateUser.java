package com.octo.authenticationcleanarchi.usecases;

import com.octo.authenticationcleanarchi.usecases.model.AuthenticateUserCommand;
import com.octo.authenticationcleanarchi.usecases.model.Token;
import com.octo.authenticationcleanarchi.usecases.model.UnauthorizedException;
import com.octo.authenticationcleanarchi.usecases.ports.RandomThirtyTwoCharsGenerator;
import com.octo.authenticationcleanarchi.usecases.ports.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class AuthenticateUser {

    private final UserRepository userRepository;
    private final RandomThirtyTwoCharsGenerator randomThirtyTwoCharsGenerator;

    @Autowired
    public AuthenticateUser(UserRepository userRepository, RandomThirtyTwoCharsGenerator randomThirtyTwoCharsGenerator) {
        this.userRepository = userRepository;
        this.randomThirtyTwoCharsGenerator = randomThirtyTwoCharsGenerator;
    }

    public Token execute(AuthenticateUserCommand authenticateUserCommand) throws Exception {
        if (!userRepository.existsWithNameAndPassword(
                authenticateUserCommand.name(),
                authenticateUserCommand.password())) {
            throw new UnauthorizedException();
        };

        String randomString = randomThirtyTwoCharsGenerator.execute();

        return new Token(randomString);
    }
}
