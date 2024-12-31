# Notes informatiques

## Démarrer jupyter notebook

Pour démarrer jupyter :

```
/LOCAL/anaconda3-2017/bin/jupyter notebook
```

Puis coller l’URL dans le navigateur, par exemple :

http://localhost:8888/?token=1b9126b2e45a2747674264ced1e9094b207daa148d792f02

**Exemple.**

    wims-tmp-2019-40@g209-2:~$ /LOCAL/anaconda3-2017/bin/jupyter notebook
    [I 13:33:20.127 NotebookApp] Writing notebook server cookie secret to /run/user/1763821/jupyter/notebook_cookie_secret
    [I 13:33:21.091 NotebookApp] Serving notebooks from local directory: /export/home/users/wims/TMP/wims-tmp-2019-40
    [I 13:33:21.091 NotebookApp] 0 active kernels
    [I 13:33:21.091 NotebookApp] The Jupyter Notebook is running at: http://localhost:8888/?token=6c93b732ebb3f85066491993f3df1f2b2a47d7a76e339b2e
    [I 13:33:21.091 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 13:33:21.094 NotebookApp]
        Copy/paste this URL into your browser when you connect for the first time,
        to login with a token:
            http://localhost:8888/?token=6c93b732ebb3f85066491993f3df1f2b2a47d7a76e339b2e
    [I 13:33:21.424 NotebookApp] Accepting one-time-token-authenticated connection from ::1

Choisir l’interpréteur Python 2 :

    Kernel > Change kernel > Python 2

## Télécharger les fichiers

Les scripts pour les séances de TP sont disponibles sur github :

    git clone https://github.com/mbaudin47/otsupgalilee-eleve.git

**Exemple.**

    wims-tmp-2019-40@g209-5:~/tmp$ git clone https://github.com/mbaudin47/otsupgalilee-eleve.git
    Clonage dans 'otsupgalilee-eleve'...
    remote: Enumerating objects: 197, done.
    remote: Counting objects: 100% (197/197), done.
    remote: Compressing objects: 100% (146/146), done.
    remote: Total 197 (delta 111), reused 134 (delta 51), pack-reused 0
    Réception d'objets: 100% (197/197), 2.52 MiB | 0 bytes/s, fait.
    Résolution des deltas: 100% (111/111), fait.

## Démarrer SALOME

    /LOCAL/salome-edf
