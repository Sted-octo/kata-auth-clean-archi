namespace Domain
{
    public interface IUser
    {
        string? Name { get; set; }
        string? Password { get; set; }
    }

    public class User : IUser
    {
        public string? Name { get; set; }
        public string? Password { get; set; }
    }
}