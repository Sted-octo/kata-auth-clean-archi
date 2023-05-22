using Domain;

namespace SerenityApi.net.Controllers
{
    public class UserDto : IUser
    {
        public string? Name { get; set; }
        public string? Password { get; set; }
    }
}