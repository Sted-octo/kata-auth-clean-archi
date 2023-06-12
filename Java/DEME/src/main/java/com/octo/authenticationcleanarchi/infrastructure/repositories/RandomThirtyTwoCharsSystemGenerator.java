package com.octo.authenticationcleanarchi.infrastructure.repositories;

import com.octo.authenticationcleanarchi.usecases.ports.RandomThirtyTwoCharsGenerator;
import org.springframework.stereotype.Component;

@Component
public class RandomThirtyTwoCharsSystemGenerator implements RandomThirtyTwoCharsGenerator {
    @Override
    public String execute() {
        return "12345678901234567890123456789012";
    }
}
