#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <sys/wait.h>
#include <unistd.h>

using namespace std;

int main(){
	int pipe_t[2];
	int stat1,stat2;
	pid_t pid1, pid2; //Child PID
	char *temp[] = {0};
	pipe(pipe_t);
	pid1=fork();

	if(pid1==0)
	{
		dup2(pipe_t[1], STDOUT_FILENO);

		close(pipe_t[0]);
		close(pipe_t[1]);
		
		if(execv("./generator", temp) < 0)
		{
			perror("Execv Generator");
			exit(1);
		}
	}

	pid2=fork();
	
	if(pid2==0)
	{
		dup2(pipe_t[1], STDOUT_FILENO);

		close(pipe_t[1]);
		close(pipe_t[0]);
		
		if(execv("./consumer", temp) < 0)
		{
			perror("Execv consumer");
			exit(1);
		}
	}

	close(pipe_t[1]);
	close(pipe_t[0]);

	sleep(1);

	kill(pid1, SIGTERM);
	
	waitpid(pid1, &stat1, 0);
	cerr << "child[" << pid1 << "] exited with status " << stat1 << endl;
	
	waitpid(pid2, &stat2, 0);
	cerr << "child[" << pid2 << "] exited with status " << stat2 << endl;

return 0;
}
