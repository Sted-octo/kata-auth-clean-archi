using Domain;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tools;

namespace UseCases
{
    public class UserAccessChecker
    {
        private IUserByNameLoader _userByNameLoader;
        private RandomString _randomString;
        public UserAccessChecker(IUserByNameLoader loader, RandomString randomString) 
        {
            _userByNameLoader = loader;
            _randomString = randomString;
        }
        
        public string Check(IUser user)
        {
            if (user == null || string.IsNullOrEmpty(user.Name) || string.IsNullOrEmpty(user.Password))
                throw new ArgumentException();

            IUser userDb = _userByNameLoader.Load(user.Name);
            if (userDb == null)
                throw new ArgumentException();

            if (userDb.Password != user.Password)
                throw new AccessDeniedException();

            return _randomString.Generate(32);
        }
    }
}
