using Adapters;
using DataProviders;
using Microsoft.AspNetCore.Mvc;
using Tools;
using UseCases;

namespace SerenityApi.net.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class AuthenticationController : Controller
    {
        [HttpPost()]
        [Route("/api/auth")]
        public ActionResult<JwtToken> Authenticate(UserDto user)
        {
            IUserByNameLoader loader = new UserByNameLoader();
            try
            {

                return new JwtToken { Token = new UserAccessChecker(loader, new RandomString()).Check(user) };
            }
            catch (Exception)
            {
                return Unauthorized();
            }
        }

    }
}
