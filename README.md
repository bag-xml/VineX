<div align="center">
   <img src="https://bag-xml.com/assets/img/v-redir.png" height="160" width="160">
   <h1>VineX</h1>
</div>

<center>A server made for older versions of the iOS Vine application.</center>

## My Original Vision
I intended VineX to be a way to still be able to interact with the Vine archive in a way that makes it feel alive, instead of dead. Users should still be able to have their own accounts, be able to comment, customize their profiles, like videos, see the likes of others, but not be able to upload. The only posts available on VIneX should be those from the official Vine Archive. Furthermore I felt inspired by <a href="https://grapper.gabis.online/">https://grapper.gabis.online/</a>, which is a wrapper around the Vine API that is an alternative to the official Vine archive which is currently inaccesible.

I would've loved to finish VineX but I'm missing the time and motivation to do it. I bet there's probably anyone out there who feels more ambitioned to make this real. If you do, you're awesome by the way. If you like VineX, or want to save it for later, I'd recommend you star this repository!

## Information and Compatibility
VineX is primarily made for the Vine iOS app, version 1.1.2. It's recommended that on release, VineX may only be used with that specific version, as support for more versions will be added in the future.

This is just a flask server, therefore should then be familiar for people who've worked with flask before.

VineX will come with a tweak too, which'll support the following iOS versions:

| iOS Version  | Support status |
| ------------- | ------------- |
| iOS 5  | Not supported  |
| iOS 6  | Supported :: Tested  |
| iOS 7  | Supported :: Tested  |
| iOS 8  | Supported :: Tested  |
| iOS 9  | Supported :: Tested  |
| iOS 10  | Untested  |
| iOS 11  | Untested  |

## Roadmap
Here is a table to show what endpoints have been implemented into VineX. And what features are still due to add.

| Authentication endpoints  | Context | Status |
| ------------- | ------------- | ------------- |
| /users  | Registration  | Completed  |
| /users/authenticate [POST] | Login  | Completed  |
| /users/authenticate [DELETE]  | Log-Out  | Completed  |
| /users/forgotPassword  | Password reset  | Incomplete  |

| User Endpoints  | Context | Status |
| ------------- | ------------- | ------------- |
| /users/profiles/(User-ID)  | User Profile  | Completed  |
| /users/me | Userinfo retrieval  | Completed  |
| /users/(User-ID)  | Settings management  | Completed  |
| /users/(User-ID)/preferences  | Settings management  | Completed  |
| /users/(User-ID)/pendingNotificationsCount  | Notification indicator  | Completed  |
| /users/(User-ID)/notifications  | Notifications (Activity page)  | Completed  |
| /users/(User-ID)/following  | Following Page  | Completed  |
| /users/search/(Search query)  | User search  | Completed  |
| /users/(User-ID)/followers [GET]  | Follower Page  | Completed  |
| /users/(User-ID)/followers [POST]  | Follow a user  | Completed  |
| /users/(User-ID)/followers [DELETE]  | Unfollow a user  | Completed  |
| /users/(User-ID)/blocked/(Target-User-ID) [POST]  | Block a user  | Completed  |
| /users/(User-ID)/blocked/(Target-User-ID) [DELETE]  | Unblock a user  | Completed  |
| /users/(User-ID)/complaints/  | File a complaint  | Completed  |
| /users/(User-ID)/following/suggested/contacts  | Address Book integration  | Incomplete  |


| Timelines  | Context | Status |
| ------------- | ------------- | ------------- |
| /timelines/posts/(Post ID) | Single post | Incomplete |

| Explore  | Context | Status |
| ------------- | ------------- | ------------- |
| /explore/(app version)  | Explore page  | Incomplete  |

| Tags  | Context | Status |
| ------------- | ------------- | ------------- |
| /tags/search/(Search query)  | Hashtag search  | Incomplete  |

## Bugs
<ul>
   <li>Follower and following pages of users have wonky indicators</li>
   <li>Notification content is blank (Yet to be fixed)</li>
</ul>

## How to use?
<ul>
<li>You need to install python, then just install the requirements. Requirements for this project are:
<ul><li>flask</li>
<li>other</li>
</ul>
</ul>
