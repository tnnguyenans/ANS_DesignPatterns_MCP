# ANS Design Patterns MCP Server

## Project Overview

The ANS Design Patterns MCP Server is a Python implementation of a Model Context Protocol (MCP) server that provides design pattern documentation. The server responds to requests for specific design patterns by returning their markdown content, making it easy to integrate design pattern knowledge into AI tools like Windsurf.

## Features

- MCP server implementation using FastMCP
- Design pattern documentation in markdown format
- Cross-platform configuration
- Direct testing capabilities
- Integration with Windsurf and other AI tools

## Available Design Patterns

### Creational Patterns
- Abstract Factory Pattern
- Builder Pattern
- Factory Method Pattern
- Prototype Pattern
- Singleton Pattern (with Thread-Safe variant)

### Structural Patterns
- Adapter Pattern
- Bridge Pattern
- Composite Pattern
- Decorator Pattern
- Facade Pattern
- Flyweight Pattern
- Proxy Pattern

### Behavioral Patterns
- Chain of Responsibility Pattern
- Command Pattern
- Iterator Pattern
- Mediator Pattern
- Memento Pattern
- Observer Pattern
- State Pattern
- Strategy Pattern
- Template Method Pattern
- Visitor Pattern

### Real-World Implementations
- Builder (Real World)
- Singleton (Real World)
- Visitor (Real World)

## Directory Structure

```
ANS_DesignPatterns_MCP/
├── server.py              # MCP server implementation
├── direct_test.py         # Script for direct testing
├── mcp-config.js          # Configuration script
├── config.json            # Server configuration
├── design-patterns/       # Directory containing design pattern documentation
│   ├── AbstractFactory.md # Abstract Factory pattern documentation
│   ├── Adapter.md         # Adapter pattern documentation
│   ├── Bridge.md          # Bridge pattern documentation
│   ├── Builder.md         # Builder pattern documentation
│   ├── ChainOfResponsibility.md # Chain of Responsibility pattern documentation
│   ├── Command.md         # Command pattern documentation
│   ├── Composite.md       # Composite pattern documentation
│   ├── Decorator.md       # Decorator pattern documentation
│   ├── Facade.md          # Facade pattern documentation
│   ├── FactoryMethod.md   # Factory Method pattern documentation
│   ├── Flyweight.md       # Flyweight pattern documentation
│   ├── Iterator.md        # Iterator pattern documentation
│   ├── Mediator.md        # Mediator pattern documentation
│   ├── Memento.md         # Memento pattern documentation
│   ├── Observer.md        # Observer pattern documentation
│   ├── Prototype.md       # Prototype pattern documentation
│   ├── Proxy.md           # Proxy pattern documentation
│   ├── Singleton.md       # Singleton pattern documentation
│   ├── SingletonThreadSafe.md # Thread-safe Singleton pattern documentation
│   ├── State.md           # State pattern documentation
│   ├── Strategy.md        # Strategy pattern documentation
│   ├── TemplateMethod.md  # Template Method pattern documentation
│   ├── Visitor.md         # Visitor pattern documentation
│   └── Real-World variants # Additional real-world implementations
└── README.md              # This file
```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Node.js (for configuration script)

### Step 1: Install Dependencies

Install the required Python packages:

```bash
pip install mcp[cli] pydantic
```

### Step 2: Configure the Server

The project includes a `config.json` file that contains the necessary configuration. If you need to modify paths or settings:

1. Open the `config.json` file in the project directory
2. Update the paths as needed for your environment:
   - `baseDir`: The base directory of the project
   - `designPatternsDir`: Directory containing the design pattern markdown files

Optionally, if you need to regenerate the configuration files for different platforms, you can run:

```bash
node mcp-config.js
```

### Step 3: Run the Server

Start the MCP server:

```bash
python server.py
```

## Using the MCP Server

### MCP Configuration

To configure the MCP server in Windsurf or other AI tools, add the following configuration to your MCP config file (typically located at `~/.codeium/windsurf/mcp_config.json` or similar):

```json
"ans-designpatterns": {
  "command": "python",
  "args": [
    "C:\\Programs\\PythonTraining\\ANS_DesignPatterns_MCP\\server.py"
  ],
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}
```

Note: Adjust the path in `args` to match your actual installation directory.

### With Windsurf

1. Ensure the MCP server is running
2. Windsurf will automatically detect and connect to the server
3. You can then request design pattern documentation through Windsurf

### Direct Testing

You can test the server directly using the provided `direct_test.py` script:

```bash
python direct_test.py
```

This will test access to the available design patterns and display their content.

### Accessing Design Patterns

The server provides the following endpoints:

- `get_design_pattern(pattern)`: Get documentation for a specific design pattern
- `design-pattern://{pattern_name}`: Resource endpoint for a specific pattern
- `patterns://list`: Resource endpoint to list all available patterns

## Adding New Design Patterns

To add a new design pattern:

1. Create a markdown file in the `design-patterns` directory (e.g., `observer.md`)
2. Follow the existing format for consistency:
   - Start with a title (e.g., `# Observer Pattern`)
   - Include sections for Intent, Code Examples, When to Use, and References
   - Provide examples in Python and/or C++

## Troubleshooting

If you encounter issues:

1. Ensure all dependencies are installed
2. Check that the configuration files are correctly set up
3. Verify that the design pattern files exist in the expected location
4. Check the server logs for any error messages

## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://creativecommons.org/licenses/by-nc-nd/4.0/).
