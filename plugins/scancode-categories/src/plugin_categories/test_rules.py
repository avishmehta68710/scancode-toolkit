{
"new_rules": [
    {
        "name": "cpp_files01",
        "test": (all(extension == resource.extension for extension in [".cpp"]) &
                    any(file_type == resource.file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files02",
        "test": (all(resource.extension == extension for extension in [".cpp"]) &
                    any(resource.file_type == file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files03",
        "test": (all(resource.extension in extension for extension in [".cpp"]) &
                    any(resource.file_type == file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files04",
        "test": (all(resource.extension in extension for extension in [".cppppppppp"]) &
                    any(resource.file_type == file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files05",
        "test": (all(resource.extension in extension for extension in [".pcppppppppp"]) &
                    any(resource.file_type == file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files06",
        "test": (all(resource.extension in extension for extension in [".pcppppppppp"]) |
                    any(resource.file_type == file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    },
    {
        "name": "cpp_files07",
        "test":
            (
                all(resource.extension in extension for extension in [".pcppppppppp"]) |
                any(resource.file_type == file_type for file_type in ["C source, ASCII text"])
            ),
        "domain": "general",
        "status": "This is core, dude!"
    },
    {
        "name": "cpp_files08",
        "test": (any(extension == resource.extension for extension in [".cpp", ".js"]) &
                    any(file_type == resource.file_type for file_type in ["C source, ASCII text"])),
        "domain": "general",
        "status": "core"
    }
]
}
