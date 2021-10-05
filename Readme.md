Pruebe los contenedores de desarrollo: Python
Un contenedor de desarrollo es un contenedor Docker en ejecución con una pila de herramientas / tiempo de ejecución bien definida y sus requisitos previos. Puede probar contenedores de desarrollo con GitHub Codespaces o Visual Studio Code Remote - Containers .

Este es un proyecto de muestra que le permite probar cualquiera de las opciones en unos sencillos pasos. También tenemos una variedad de otros proyectos de muestra de vscode-remote-try- * .

Nota: Si ya tiene un espacio de código o un contenedor de desarrollo, puede saltar a la sección Cosas para probar .

Configurar el contenedor de desarrollo
Espacios de códigos de GitHub
Siga estos pasos para abrir esta muestra en un espacio de código:

Haga clic en el menú desplegable Código y seleccione la opción Abrir con espacios de código .
Seleccione + Nuevo espacio de código en la parte inferior del panel.
Para obtener más información, consulte la documentación de GitHub .

VS Code Remote - Contenedores
Siga estos pasos para abrir esta muestra en un contenedor usando la extensión VS Code Remote - Containers:

Si es la primera vez que usa un contenedor de desarrollo, asegúrese de que su sistema cumpla con los requisitos previos (es decir, tenga Docker instalado) en los pasos de introducción .

Para usar este repositorio, puede abrir el repositorio en un volumen Docker aislado:

Presione F1y seleccione el comando Contenedores remotos: Pruebe una muestra ...
Elija la muestra "Python", espere a que se inicie el contenedor y pruebe las cosas.
Nota: Bajo el capó, esto usará el comando Remote-Containers: Clone Repository in Container Volume ... para clonar el código fuente en un volumen Docker en lugar del sistema de archivos local. Los volúmenes son el mecanismo preferido para conservar los datos del contenedor.

O abra una copia clonada localmente del código:

Clone este repositorio en su sistema de archivos local.
Presione F1y seleccione el comando Contenedores remotos: Abrir carpeta en contenedor ...
Seleccione la copia clonada de esta carpeta, espere a que se inicie el contenedor y pruebe las cosas.
Cosas para probar
Una vez que haya abierto esta muestra, podrá trabajar con ella como lo haría localmente.

Nota: este contenedor se ejecuta como un usuario no root con acceso sudo de forma predeterminada. Comentar "remoteUser": "vscode"en .devcontainer/devcontainer.jsonsi prefiere ejecutar como root.

Algunas cosas para probar:

Editar:

Abierto app.py
Intente agregar un código y verifique las características del idioma.
Terminal:

Presione ctrl+ shift+ `para abrir una ventana de terminal.

Escriba python -m flask run --port 9000 --no-debugger --no-reloadpara ejecutar la aplicación.

La terminal dirá que su aplicación es Running on http://127.0.0.1:9000/. Haga clic en el enlace en la terminal para ver su aplicación ejecutándose en el navegador.
Tenga en cuenta que la extensión de Python ya está instalada en el contenedor, ya que la .devcontainer/devcontainer.jsonlista "ms-python.python"como una extensión para instalar automáticamente cuando se crea el contenedor.

Consejo: si usa este contenedor fuera de VS Code a través de docker runcon -p 9000, es posible que deba agregar --host 0.0.0.0el comando anterior. La -popción "publica" el puerto en lugar de reenviarlo. Por lo tanto, no funcionará si la aplicación solo escucha localhost. La forwardPortspropiedad en devcontainer.jsonno tiene esta limitación, pero puede usar la appPortpropiedad en su lugar si desea reflejar el docker runcomportamiento.

Compilar, ejecutar y depurar:

Abierto app.py
Agregue un punto de interrupción (por ejemplo, en la línea 9).
Presione F5para iniciar la aplicación en el contenedor.
Una vez que se alcanza el punto de interrupción, intente desplazarse sobre las variables (por ejemplo, la variable de la aplicación en la línea 7), examinar los locales y más.
Continuar ( F5). Puede conectarse al servidor en el contenedor mediante:
Al hacer clic en Open in Browserla notificación que le dice: Your service running on port 9000 is available.
Haciendo clic en el icono del globo terráqueo en la vista 'Puertos'. La vista 'Puertos' le brinda una tabla organizada de sus puertos reenviados, y puede acceder a ella con el comando Puertos: Enfoque en la vista de puertos .
Observe que el puerto 9000 en la vista 'Puertos' tiene la etiqueta "Hola mundo remoto". En devcontainer.json, puede establecer "portsAttributes", como una etiqueta para sus puertos reenviados y la acción que se tomará cuando el puerto se reenvíe automáticamente.
Nota: En Remote - Containers, puede acceder a su aplicación http://localhost:9000en un navegador local. Pero en un espacio de código basado en navegador, debe hacer clic en el enlace de la notificación o la Portsvista para que el servicio maneje el reenvío de puertos en el navegador y genere la URL correcta.

Reconstruya o actualice su contenedor

Es posible que desee realizar cambios en su contenedor, como instalar una versión diferente de un software o reenviar un nuevo puerto. Reconstruirá su contenedor para que los cambios surtan efecto.

Abrir navegador automáticamente: como cambio de ejemplo, actualice el portsAttributesen el .devcontainer/devcontainer.jsonarchivo para abrir un navegador cuando nuestro puerto se reenvíe automáticamente.

Abra el .devcontainer/devcontainer.jsonarchivo.
Modifique el "onAutoForward"atributo en su portsAttributesdesde "notify"a "openBrowser".
Presione F1y seleccione el comando Remote-Containers: Rebuild Container o Codespaces: Rebuild Container para que se recojan las modificaciones.
Más muestras
Aplicación Tweeter: Python y Django
Contribuyendo
Este proyecto agradece contribuciones y sugerencias. La mayoría de las contribuciones requieren que acepte un Acuerdo de licencia de colaborador (CLA) que declara que tiene derecho a otorgarnos, y que realmente lo hace, los derechos para utilizar su contribución. Para obtener más información, visite https://cla.microsoft.com .

Cuando envíe una solicitud de extracción, un CLA-bot determinará automáticamente si necesita proporcionar un CLA y decorar el PR de manera adecuada (por ejemplo, etiqueta, comentario). Simplemente siga las instrucciones proporcionadas por el bot. Solo necesitará hacer esto una vez en todos los repositorios usando nuestro CLA.

Este proyecto ha adoptado el Código de conducta de código abierto de Microsoft . Para obtener más información, consulte las preguntas frecuentes sobre el Código de conducta o póngase en contacto con opencode@microsoft.com si tiene preguntas o comentarios adicionales.

Licencia
Copyright © Microsoft Corporation Todos los derechos reservados.
Licenciado bajo la licencia MIT. Consulte LICENCIA en la raíz del proyecto para obtener información sobre la licencia
