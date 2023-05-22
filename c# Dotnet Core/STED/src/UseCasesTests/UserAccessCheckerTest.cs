using Domain;
using Moq;
using Tools;
using UseCases;

namespace UseCasesTests
{
    public class UserAccessCheckerTest
    {
        [Fact]
        public void Test_No_Name_No_Password_should_return_Argument_Exception()
        {
            IUser userToCheck = new User();
            Mock<IUserByNameLoader> loader = new Mock<IUserByNameLoader>();
            loader.Setup(l=>l.Load("")).Returns<IUser?>(null);

            Assert.Throws<ArgumentException>(() => new UserAccessChecker(loader.Object, new Tools.RandomString()).Check(userToCheck));
        }

        [Fact]
        public void Test_Unknown_Name_should_return_Error_Argument_Exception()
        { 
            IUser userToCheck = new User { Name="debra" };
            Mock<IUserByNameLoader> loader = new Mock<IUserByNameLoader>();
            loader.Setup(l => l.Load("debra")).Returns<IUser?>(null);

            Assert.Throws<ArgumentException>(() => new UserAccessChecker(loader.Object, new Tools.RandomString()).Check(userToCheck));
        }

        [Fact]
        public void Test_known_Name_With_Known_Password_should_return_Valid_Token()
        { 
            IUser userToCheck = new User { Name = "dexter", Password = "killer" };
            Mock<IUserByNameLoader> loader = new Mock<IUserByNameLoader>();
            loader.Setup(l => l.Load("dexter")).Returns(new User { Name = "dexter", Password = "killer" });

            string token = new UserAccessChecker(loader.Object, new Tools.RandomString()).Check(userToCheck);

            Assert.Equal(32, token.Length);
        }

        [Fact]
        public void Test_known_Name_With_Wrong_Password_should_return_Error_Access_Denied()
        {
            IUser userToCheck = new User { Name = "dexter", Password = "morgan" };
            Mock<IUserByNameLoader> loader = new Mock<IUserByNameLoader>();
            loader.Setup(l => l.Load("dexter")).Returns(new User { Name = "dexter", Password = "killer" });

            Assert.Throws<AccessDeniedException>(() => new UserAccessChecker(loader.Object, new Tools.RandomString()).Check(userToCheck));
        }
    }
}