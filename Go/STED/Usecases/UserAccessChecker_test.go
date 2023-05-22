package Usecases

import (
	"fmt"
	"serenityapi/Domain"
	"testing"

	"github.com/stretchr/testify/assert"
)

var mockLoader IUserByNameLoader = new(Mock_UserByNameLoader)

func Test_No_Name_No_Password_should_return_Error_Access_Denied(t *testing.T) {
	user := Domain.User{Name: "", Password: ""}

	_, err := UserAccessChecker(user, mockLoader)

	assert.EqualError(t, err, ACCESS_DENIED_ERROR)
}

func Test_Unknown_Name_should_return_Error_Access_Denied(t *testing.T) {
	user := Domain.User{Name: "debra", Password: ""}

	_, err := UserAccessChecker(user, mockLoader)

	assert.EqualError(t, err, ACCESS_DENIED_ERROR)
}

func Test_known_Name_With_Known_Password_should_return_Valid_Token(t *testing.T) {
	user := Domain.User{Name: "dexter", Password: "killer"}

	token, err := UserAccessChecker(user, mockLoader)

	assert.NoError(t, err)
	assert.Equal(t, 32, len(token), fmt.Sprintf("Token length should be 32 be was %d", len(token)))
}

func Test_known_Name_With_Wrong_Password_should_return_Error_Access_Denied(t *testing.T) {
	user := Domain.User{Name: "dexter", Password: "morgan"}

	_, err := UserAccessChecker(user, mockLoader)

	assert.EqualError(t, err, ACCESS_DENIED_ERROR)
}
