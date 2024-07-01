
1. Hacer cambios al proyecto, y crear una rama para poder guardarlos.
    Para crear una rama, debemos usar el comando:

       git branch nombreRama

    Luego de crear una rama, hay que cambiarse a la rama que se creó, usando el comando

       git checkout nombreRama
   
3. Una vez que tenemos nuestra rama, procedemos a guardar los cambios que necesitamos usar en un commit.

   Aqui tenemos una imagen explicando en Visual Code donde tenemos los archivos que se guardarán en un commit.
![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/f98f805e-027c-4f93-960c-1d3b981652a7)

5. Para poder subir los cambios a la rama main del github, primero necesitamos que nuestra rama esté con los ultimos cambios de main de Github.
    Para poder descargar los ultimos cambios, usamos:

       git pull origin master

    ** Si hay error cuando se baja la rama (por motivo de conflictos), debemos hacer lo siguiente:**

       a) Cambiarse a la rama local de main
           git checkout RAMA_MAIN
      
        b) En la rama de main hacerle un
           git pull origin main
      
        c) Cambiarse a la rama de los cambios, y hacerle un
           git merge RAMA_MAIN
      
        d) Arreglar los conflictos, y hacer commit a los archivos afectados
      
6. Luego de tener los cambios que se han estado desarrollando, junto con los cambios en main de Github (rama main remote), se debe proceder a subir los cambios al servidor, con

       git push -f origin RAMALOCAL:RAMAREMOTA

   Este comando lo que hará será crear una rama en el servidor de Github con tus cambios.

7. Después de crear la rama en Github, se procede crear un Pull Request para que tus cambios se reflejen en la rama MAIN
    ![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/4c5ed39f-6f4b-4c03-a03e-41c66c8907ac)

Escojemos la rama que deseamos que se refleje en la rama Main
    
![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/af2c7a73-02b7-4213-a5e5-dd7c5d15eeda)

En la siguiente pagina que se muestra, podemos observar los cambios que se han trabajado en la rama, y procedemos a crear el Pull Request.

![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/cca4ee12-ee8f-489c-9f01-68b7dcaf28d5)

En la parte izquierda de la pagina, debemos ponerle un titulo y una descripcion sobre el Pull Request (PR). Y en la derecha debemos asignarnos a nosotros mismos, y debemos asignar a un "Reviewer", para que revise nuestro codigo y cambios (puede ser un QA u otro Desarrollador).
![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/a997490d-3500-4056-b326-08936c0ac8a5)

![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/019d4e66-24f5-4022-b671-7ce0b501c0e6)

8. Cuando el PR esté creado, se debe pedir al **devops** para que ayude a aprobar los cambios subidos.
    Observamos que el PR está Inhabilitado para los desarrolladores, debido a las reglas que se personalizaron para el proyecto (https://github.com/gusugus/GestionConfiguracion2024S1/settings/rules)
   
![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/89378292-373b-49f9-a096-1b023e965fdd)

![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/13c7f0a0-a111-40ac-aa7b-c2a83f2f1796)

9. Observamos que el PR esta merged y que los cambios estan en la rama Principal (main)

![imagen](https://github.com/gusugus/GestionConfiguracion2024S1/assets/5783772/c0459090-0fed-4096-bd86-68a76457c80d)
