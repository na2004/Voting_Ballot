# Root the (Ballot) Box

This is the base system for the e-voting project.

It's not very secure by default. This was _not_ written with best practices
in mind, so in your testing you should see if the base system itself could be
vulnerable to an attack!

## Running the Front-End

The front-end interface to the voting machine is a series of CGI
applications, written in both Bash and in Python. From the root of the
folder, run

```sh
$ make cgi
```

This starts a CGI-aware web server running on port 8000 on the local machine.
Then, using a web browser, go to `http://localhost:8000/cgi-bin/home.cgi` to
access the interface. The default password for the login system is `admin`.
If you wish to add additional CGI scripts, add them to the `cgi-bin/`
directory, making sure you mark them as executable (`chmod 755 file.cgi`). To
exit the CGI server, send a keyboard interupt (`<Ctrl>+C`).


