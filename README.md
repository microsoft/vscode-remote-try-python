# Try Out Development Containers: Python

A **development container** is a running [Docker](https://www.docker.com) container with a well-defined tool/runtime stack and its prerequisites. You can try out development containers with **[GitHub Codespaces](https://github.com/features/codespaces)** or **[Visual Studio Code Remote - Containers](https://aka.ms/vscode-remote/containers)**.

This is a sample project that lets you try out either option in a few easy steps. We have a variety of other [vscode-remote-try-*](https://github.com/search?q=org%3Amicrosoft+vscode-remote-try-&type=Repositories) sample projects, too.

> **Note:** If you already have a Codespace or dev container, you can jump to the [Things to try](#things-to-try) section. 

## Setting up the development container

### GitHub Codespaces
Follow these steps to open this sample in a Codespace:
1. Click the Code drop-down menu and select the **Open with Codespaces** option.
1. Select **+ New codespace** at the bottom on the pane.

For more info, check out the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/developing-online-with-codespaces/creating-a-codespace#creating-a-codespace).

### VS Code Remote - Containers
Follow these steps to open this sample in a container using the VS Code Remote - Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in the [getting started steps](https://aka.ms/vscode-remote/containers/getting-started).

2. To use this repository, you can either open the repository in an isolated Docker volume:

    - Press <kbd>F1</kbd> and select the **Remote-Containers: Try a Sample...** command.
    - Choose the "Python" sample, wait for the container to start, and try things out!
        > **Note:** Under the hood, this will use the **Remote-Containers: Clone Repository in Container Volume...** command to clone the source code in a Docker volume instead of the local filesystem. [Volumes](https://docs.docker.com/storage/volumes/) are the preferred mechanism for persisting container data.   

   Or open a locally cloned copy of the code:

   - Clone this repository to your local filesystem.
   - Press <kbd>F1</kbd> and select the **Remote-Containers: Open Folder in Container...** command.
   - Select the cloned copy of this folder, wait for the container to start, and try things out!

## Things to try

Once you have this sample opened, you'll be able to work with it like you would locally.

> **Note:** This container runs as a non-root user with sudo access by default. Comment out `"remoteUser": "vscode"` in `.devcontainer/devcontainer.json` if you'd prefer to run as root.

Some things to try:

1. **Edit:**
   - Open `app.py`
   - Try adding some code and check out the language features.

2. **Terminal:** 
    - Press <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>\`</kbd> to open a terminal window.
    - Type `python -m flask run --port 9000 --no-debugger --no-reload` to run the app.
         - The terminal will say your app is `Running on http://127.0.0.1:9000/`. Click on the link in the terminal to view your app running in the browser.
    - Notice that the Python extension is already installed in the container since the `.devcontainer/devcontainer.json` lists `"ms-python.python"` as an extension to install automatically when the container is created.
    
      > **Tip:** If you use this container outside of VS Code via `docker run` with `-p 9000`, you may need to append `--host 0.0.0.0` to the command above. The `-p` option "publishes" the port rather than forwarding it. It therefore will not work if the application only listens to localhost. The `forwardPorts` property in `devcontainer.json` does not have this limitation, but you can use `appPort` property instead if you want to mirror the `docker run` behavior.

3. **Build, Run, and Debug:**
   - Open `app.py`
   - Add a breakpoint (e.g. on line 9).
   - Press <kbd>F5</kbd> to launch the app in the container.
   - Once the breakpoint is hit, try hovering over variables (e.g. the app variable on line 7), examining locals, and more.
   - Continue (<kbd>F5</kbd>). You can connect to the server in the container by either: clicking on `Running on http://0.0.0.0:9000/` in the terminal output, or "Open in Browser" next to port 9000 in the 'Ports' view (you can get to the 'Ports' view by clicking on the "1" in the status bar, which means your app has 1 forwarded port).
   
   > **Note:** In Remote - Containers, you can access your app at `http://localhost:9000` in a local browser. But in a browser-based Codespace, you must click the link from the terminal output or the `Ports` view so that the service handles port forwarding in the browser and generates the correct URL.

4. **Rebuild or update your container** (*Currently, only containers with the VS Code Remote - Containers extension can be rebuilt.*)

   You may want to make changes to your container, such as installing a different version of a software or forwarding a new port. You'll rebuild your container for your changes to take effect. 

   **Forward a port statically:** As an example change, let's forward a port statically in the `.devcontainer/devcontainer.json` file. 

   > **Note:** Remote-Containers and Codespaces also take care of dynamic port forwarding, but there may be instances in which we want to statically declare a forwarded port. 
   
   - Open the `.devcontainer/devcontainer.json` file.
   - Uncomment the `forwardedPorts` attribute and adjust the port number as needed.
   - Press <kbd>F1</kbd> and select the **Remote-Containers: Rebuild Container** command so the modifications are picked up.  

### More samples

- [Tweeter App - Python and Django](https://github.com/Microsoft/python-sample-tweeterapp)

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## License

Copyright © Microsoft Corporation All rights reserved.<br />
Licensed under the MIT License. See LICENSE in the project root for license information.
