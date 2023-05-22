using Domain;
using UseCases;

namespace DataProviders
{
    public class UserByNameLoader : IUserByNameLoader
    {
        public IUser? Load(string name)
        {
            if (name == null)
                return null;
            if (name == "dexter")
                return new User { Name = "dexter", Password = "killer" };

            return null;
        }
    }
}