from docker.client import DockerClient

def check_running_docker(client:DockerClient):
	print("List of current docker containers.")
	for container in client.containers.list(all=True):
		if container.status == 'running':
			# print(f"[{container.id}] {container.name} ({container.status})")
			print(f"\t[{container.name}] {container.status}")


def docker_exec(client:DockerClient, contain_container_name:str, cmd:str, user:str):
	"""
	현재 실행중인 docker container의 이름과 일치한 container에 exec 를 수행함
	:param client:
	:param contain_container_name:
	:return:
	"""
	# print(f"... contain_container_name: {contain_container_name}")
	# print(f"... cmd : {cmd}")
	for container in client.containers.list(all=True):
		if container.status == 'running' and container.name.find(contain_container_name) > 0:
			print(f"[{container.name}] {container.status}")
			if user:
				print(f'\t-user: {user}')
				_, stream = container.exec_run(cmd=cmd, stream=True, user=user)
			else:
				_, stream = container.exec_run(cmd=cmd, stream=True)
			for data in stream:
				print(data.decode())
			print("="*100)
	print("DONE!")

if __name__ == "__main__":
	import docker

	client = docker.from_env()
	# docker_exec(client=client, contain_container_name="worker", cmd='pip list')
	check_running_docker(client=client)