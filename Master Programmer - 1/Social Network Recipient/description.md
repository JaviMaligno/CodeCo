# Challenge description

In a social network all message recipients are identified by preceding their username with the '@' symbol.

* Recipients can occur at any point in the message
* Usernames can contain letters, numbers, underscores and hyphens
* Any character which is not a valid username character will separate the recipients from the rest of the message
* Email addresses should not be matched as usernames

Create a method which can return the username of the nth recipient in the message. *n* is the (1 based) position of the recipient in the message. The method should receive two parameters - the message and the position of the recipient. If the recipient isn't found then the method should return an empty string. For example:

```
var message = "@User_One @UserABC! Have you seen this from @Userxyz?";
GetRecipient(message,1)="User_One";
GetRecipient(message, 2)="UserABC";
GetRecipient(message, 3)="Userxyz";
GetRecipient(message, 4)="";
```
