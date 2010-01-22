from fabric.api import env, run, sudo

env.user = 'username here'
env.hosts = ['hostname here']

def update():
        """Updates the code from the repository."""

        # Update the code.
        run("cd /path/on/server/; git pull origin master")

        # Restart lighttpd.
        restart_lighttpd()
        
def restart_lighttpd():
        sudo('/etc/init.d/lighttpd restart')