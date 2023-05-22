package Usecases

import (
	"errors"
	"serenityapi/Domain"
	"serenityapi/Tools"
)

const ACCESS_DENIED_ERROR string = "acess denied"

func UserAccessChecker(user Domain.User, loaderByName IUserByNameLoader) (string, error) {
	token := ""
	if user.Name == "" || user.Password == "" {
		return token, errors.New(ACCESS_DENIED_ERROR)
	}

	userDb := loaderByName.Load(user.Name)

	if userDb == nil {
		return token, errors.New(ACCESS_DENIED_ERROR)
	}

	if user.Password != userDb.Password {
		return token, errors.New(ACCESS_DENIED_ERROR)
	}

	return Tools.RandStringBytes(32), nil
}
