package Controllers

import (
	"serenityapi/Domain"
)

// UserDto is just a data trasfert struct to receive datas from a json file
type UserDto struct {
	Domain.User
}
