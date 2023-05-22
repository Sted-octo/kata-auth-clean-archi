package Usecases

import "serenityapi/Domain"

type IUserByNameLoader interface {
	Load(string) *Domain.User
}
