import subprocess


def patch_arguments(function, **patched_kwargs):
    def decorate_name(*args, **kwargs):
        kwargs.update(patched_kwargs)
        return function(*args, **kwargs)

    return decorate_name


def main(*args, **kwargs):

    # Monkey-patch to avoid ffmpeg/ffprobe calls opening console window
    subprocess.Popen = patch_arguments(
        subprocess.Popen, creationflags=subprocess.CREATE_NO_WINDOW
    )

    import nbswave

    nbswave.render_audio(*args, **kwargs)


if __name__ == "__main__":
    main()
