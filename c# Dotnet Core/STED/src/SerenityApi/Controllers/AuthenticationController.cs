using Adapters;
using Microsoft.AspNetCore.Mvc;
using UseCases;

namespace SerenityApi.net.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuthenticationController : Controller
    {
        private UserAccessChecker _userAccessChecker;
        public AuthenticationController( UserAccessChecker userAccessChecker) 
        {
            _userAccessChecker = userAccessChecker;
        }

        [HttpPost()]
        [Route("/api/auth")]
        public ActionResult<JwtToken> Authenticate(UserDto user)
        {
            try
            {
                return new JwtToken { Token = _userAccessChecker.Check(user) };
            }
            catch (Exception)
            {
                return Unauthorized();
            }
        }
    }
}
