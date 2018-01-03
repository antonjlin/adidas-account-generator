# adidas-account-generator

An Adidas.com account generator that creates accounts without requiring a captcha harvester of any sort (manual captcha harvesting, 2captcha, or anti-captcha).
*Exports account info to a .txt file ```createdaccounts.txt```
* NOTE: This currently does not support proxies. In an effort to not get softbanned by adidas, it it not threaded. The code is there for proxy and threading but it's still buggy and in development. Feel free to contribute. If you put proxies into the file it will automatically use them and start threading (untested).
* Proxies can be ip or user/pass verified.

## Make login links
To make login links, copy and paste this link into your browser.
```
https://cp.adidas.com/idp/startSSO.ping?username=[MYEMAIL]&password=[MYPASSWORD]&signinSubmit=Sign+in&IdpAdapterId=adidasIdP10&SpSessionAuthnAdapterId=https%3A%2F%2Fcp.adidas.com%2Fweb%2F&PartnerSpId=sp%3Ademandware&validator_id=adieComDWgb&TargetResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2FMyAccount-ResumeLogin&target=account&InErrorResource=https%3A%2F%2Fwww.adidas.com%2Fon%2Fdemandware.store%2FSites-adidas-US-Site%2Fen_US%2Fnull&loginUrl=https%3A%2F%2Fcp.adidas.com%2Fweb%2FeCom%2Fen_US%2Floadsignin&cd=eCom%7Cen_US%7Ccp.adidas.com%7Cnull&remembermeParam=&app=eCom&locale=US&domain=cp.adidas.com&pfRedirectBaseURL_test=https%3A%2F%2Fcp.adidas.com&pfStartSSOURL_test=https%3A%2F%2Fcp.adidas.com%2Fidp%2FstartSSO.ping%3F&resumeURL_test=&FromFinishRegistraion=&CSRFToken=null
  ```
* Replace ```[MYEMAIL]``` with your email and ```[MYPASSWORD]``` with your password.
* The page should automatically log you into the account.

### Prerequisites

1. Clone the repository
2. Install the dependencies
3. Requires python 3+
```
pip3 install requests
pip3 install bs4
```
4. cd into the folder you cloned the repo in.
```
python3 accountgen.py
```

## ToDo
- [X] Account creation
- [ ] Threading and proxies
- [ ] Support for different regions (EU, UK, GE)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Feel free to contribute to this!
* Made by [Anton Lin]
