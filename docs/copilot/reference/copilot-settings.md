---
ContentId: 7b232695-cbbe-4f3f-a625-abc7a5e6496c
DateApproved: 06/12/2025
MetaDescription: Overview of the configuration settings for GitHub Copilot in Visual Studio Code.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# GitHub Copilot in VS Code settings reference

This article lists the configuration settings for GitHub Copilot in Visual Studio Code. For general information about working with settings in VS Code, refer to [User and workspace settings](/docs/configure/settings.md), as well as the [Variables reference](/docs/reference/variables-reference.md) for information about predefined variable support.

> [!TIP]
> If you don't yet have a Copilot subscription, you can use Copilot for free by signing up for the [Copilot Free plan](https://github.com/github-copilot/signup) and get a monthly limit of completions and chat interactions.

The team is continuously working on improving Copilot in VS Code and adding new features. Some features are still experimental. Try them out and share your feedback in [our issues](https://github.com/microsoft/vscode-copilot-release/issues). Get more info about the [feature lifecycle in VS Code](/docs/configure/settings.md#feature-lifecycle).

## General settings

* `setting(github.copilot.editor.enableCodeActions)`: Controls if Copilot commands are shown as Code Actions when available.
* `setting(github.copilot.renameSuggestions.triggerAutomatically)`: Controls whether Copilot generates suggestions for renaming.
* `setting(chat.commandCenter.enabled)`: Controls whether to show the Copilot menu in the VS Code title bar (default: `true`).
* `setting(workbench.commandPalette.experimental.askChatLocation)` _(Experimental)_: Controls where the Command Palette should ask chat questions.
* `setting(search.searchView.semanticSearchBehavior)` _(Preview)_: Configure when to run semantic search in the Search view: manually (default), when no text search results are found, or always.
* `setting(search.searchView.keywordSuggestions)` _(Preview)_: Controls whether to show keyword suggestions in the Search view. This setting is disabled by default.
* `setting(workbench.settings.showAISearchToggle)` _(Experimental)_: Enable searching settings with AI in the Settings editor. This setting is enabled by default.

## Code completion settings

* `setting(github.copilot.enable)`: Enable or disable Copilot completions for specified [languages](/docs/languages/identifiers.md).
* `setting(github.copilot.nextEditSuggestions.enabled)`: Enables Copilot next edit suggestions (Copilot NES).
* `setting(editor.inlineSuggest.edits.allowCodeShifting)`: Configure if Copilot NES is able to shift your code to show a suggestion.
* `setting(editor.inlineSuggest.edits.renderSideBySide)`: Configure if Copilot NES can show larger suggestions side-by-side if possible, or if Copilot NES should always show larger suggestions below the relevant code.

## Chat settings

* `setting(github.copilot.chat.followUps)`: Controls whether Copilot should suggest follow-up questions in chat.
* `setting(github.copilot.chat.localeOverride)`: Specify a locale that Copilot should respond in, such as `en` or `fr`.
* `setting(github.copilot.chat.runCommand.enabled)`: Enables the `/runCommand` intent in the Chat view to run VS Code commands.
* `setting(github.copilot.chat.useProjectTemplates)`: Use relevant GitHub projects as starter projects when using `/new`.
* `setting(github.copilot.chat.scopeSelection)`: Whether to prompt for a specific symbol scope if you use `/explain` and the active editor has no selection.
* `setting(github.copilot.chat.terminalChatLocation)`: Controls where chat queries from the terminal should be opened.
* `setting(chat.detectParticipant.enabled)`: Enable chat participant detection in the Chat view.
* `setting(chat.editor.fontFamily)`: Font family in chat codeblocks.
* `setting(chat.editor.fontSize)`: Font size in pixels in chat codeblocks.
* `setting(chat.editor.fontWeight)`: Font weight in chat codeblocks.
* `setting(chat.editor.lineHeight)`: Line height in pixels in chat codeblocks.
* `setting(chat.editor.wordWrap)`: Toggle line wrapping in chat codeblocks.
* `setting(chat.editing.confirmEditRequestRemoval)`: Ask for confirmation before undoing an edit (default: `true`)
* `setting(chat.editing.confirmEditRequestRetry)`: Ask for confirmation before performing a redo of the last edit (default: `true`)
* `setting(chat.editing.autoAcceptDelay)`: Configure a delay after which suggested edits are automatically accepted, use zero to disable auto-accept (default: 0)
* `setting(chat.agent.enabled:true)`: Enable or disable agent mode (default: `false`, requires VS Code 1.99 or later)
* `setting(chat.agent.maxRequests)`: Maximum number of requests that Copilot can make in agent mode (default: 15)
* `setting(github.copilot.chat.agent.autoFix)`: Automatically diagnose and fix issues in the generated code changes (default: `true`)
* `setting(github.copilot.chat.agent.runTasks)`: Run workspace tasks when using agent mode (default: `true`)
* `setting(chat.mcp.enabled)` _(Preview)_: Enable Model Context Protocol (MCP) support in VS Code. This enables adding tools from MCP servers in agent mode.
* `setting(github.copilot.chat.codesearch.enabled)` _(Preview)_: When using `#codebase` in the prompt, Copilot automatically discovers relevant files to be edited.
* `setting(chat.implicitContext.enabled)` _(Experimental)_: Configure if the active editor should be automatically added as context to the chat prompt.
* `setting(github.copilot.chat.agent.thinkingTool:true)` _(Experimental)_: Enable the thinking tool in agent mode.
* `setting(github.copilot.chat.newWorkspaceCreation.enabled)` _(Experimental)_: Enable the agent mode tool for scaffolding a new workspace in chat.
* `setting(github.copilot.chat.edits.temporalContext.enabled)` _(Experimental)_: Whether to include recently viewed and edited files with requests in Copilot Edits.
* `setting(github.copilot.chat.edits.suggestRelatedFilesFromGitHistory)` _(Experimental)_: Suggest related files from git history in Copilot Edits (default: `false`)
* `setting(chat.tools.autoApprove)` _(Experimental)_: Automatically approve all tools (default: `false`)
* `setting(chat.sendElementsToChat.enabled)` _(Experimental)_: Enable sending elements from the Simple Browser to the chat view as context (default: `true`).

## Inline chat settings

* `setting(inlineChat.acceptedOrDiscardBeforeSave)`: Controls whether pending Inline Chat sessions in an editor prevent saving the file.
* `setting(inlineChat.finishOnType)`: Whether to finish an Inline Chat session when typing outside of changed regions.
* `setting(inlineChat.holdToSpeech)`: Whether holding the Inline Chat keyboard shortcut will automatically enable speech recognition.
* `setting(inlineChat.lineEmptyHint)` _(Experimental)_: Controls whether to show a hint for Inline Chat on an empty line.
* `setting(inlineChat.lineNaturalLanguageHint)` _(Experimental)_: Experimental suggestion that triggers Inline Chat as soon as a line mostly consists of words.
* `setting(editor.inlineSuggest.syntaxHighlightingEnabled)`: Controls whether to show syntax highlighting for inline suggestions.
* `setting(github.copilot.chat.editor.temporalContext.enabled)` _(Experimental)_: Whether to include recently viewed and edited files with Copilot requests in Inline Chat.

## Customize chat

* `setting(github.copilot.chat.codeGeneration.useInstructionFiles)`: Controls whether code instructions from `.github/copilot-instructions.md` are added to Copilot requests.
* `setting(github.copilot.chat.reviewSelection.enabled)` _(Preview)_: Enable code review for an editor text selection.
* `setting(github.copilot.chat.reviewSelection.instructions)` _(Preview)_: A set of instructions that will be added to Copilot requests for reviewing the current editor selection.
* `setting(github.copilot.chat.codeGeneration.instructions)` _(Experimental)_: A set of instructions that will be added to Copilot requests that generate code.
* `setting(github.copilot.chat.testGeneration.instructions)` _(Experimental)_: A set of instructions that will be added to Copilot requests that generate tests.
* `setting(github.copilot.chat.commitMessageGeneration.instructions)` _(Experimental)_: A set of instructions that will be added to Copilot requests that generate commit messages.
Copilot requests for reviewing the current editor selection.
* `setting(github.copilot.chat.pullRequestDescriptionGeneration.instructions)` _(Experimental)_: A set of instructions that will be added to Copilot requests that generate pull request titles and descriptions.
* `setting(chat.promptFiles)` _(Experimental)_: Enable or disable reusable prompt files.
* `setting(chat.promptFilesLocations)` _(Experimental)_: A dictionary of folders where prompt files are located and a boolean indicating whether they are enabled. Relative paths are resolved from the root folder(s) of your workspace. Supports glob patterns for file paths.
* `setting(chat.instructionsFilesLocations)` _(Experimental)_: A dictionary of folders where instructions files are located and a boolean indicating whether they are enabled. Relative paths are resolved from the root folder(s) of your workspace. Supports glob patterns for file paths.
* `setting(chat.modeFilesLocations)` _(Experimental)_: A dictionary of folders where chat mode files are located and a boolean indicating whether they are enabled. Relative paths are resolved from the root folder(s) of your workspace. Supports glob patterns for file paths.

## Debugging settings

* `setting(github.copilot.chat.startDebugging.enabled)` _(Preview)_: Enables the experimental `/startDebugging` intent in the Chat view to generate debugging configuration.
* `setting(github.copilot.chat.copilotDebugCommand.enabled)` _(Preview)_: Enables the `copilot-debug` terminal command.

## Testing settings

* `setting(github.copilot.chat.generateTests.codeLens)` _(Experimental)_: Show **Generate tests** code lens for symbols that are not covered by current test coverage information.
* `setting(github.copilot.chat.setupTests.enabled)` _(Experimental)_: Enables the experimental `/setupTests` intent and prompting in `/tests` generation.
* `setting(github.copilot.chat.testGeneration.instructions)` _(Experimental)_: A set of instructions that will be added to Copilot requests that generate tests.

## Notebook settings

* `setting(notebook.experimental.generate)` _(Experimental)_: Enable the **Generate** action to create code cells with Inline Chat enabled in the notebook editor.

## Accessibility settings

* `setting(inlineChat.accessibleDiffView)`: Whether the Inline Chat also renders an accessible diff viewer for its changes.
* `setting(accessibility.signals.chatRequestSent)`: Plays a signal - sound (audio cue) and/or announcement (alert) - when a chat request is made.
* `setting(accessibility.signals.chatResponseReceived)`: Plays a sound / audio cue when the response has been received.
* `setting(accessibility.verbosity.inlineChat)`: Provide information about how to access the inline editor chat accessibility help menu and alert with hints that describe how to use the feature when the input is focused.
* `setting(accessibility.verbosity.inlineCompletions)`: Provide information about how to access the inline completions hover and Accessible View.
* `setting(accessibility.verbosity.panelChat)`: Provide information about how to access the chat help menu when the chat input is focused.
* `setting(accessibility.voice.keywordActivation)`: Controls whether the keyword phrase 'Hey Code' is recognized to start a voice chat session.
* `setting(accessibility.voice.autoSynthesize)`: Controls whether a textual response should automatically be read out aloud when speech was used as input.
* `setting(accessibility.voice.speechTimeout)`: The duration in milliseconds that voice speech recognition remains active after you stop speaking.

## Related resources

* [Get a quick overview of the Copilot features in VS Code](/docs/copilot/reference/copilot-vscode-features.md)
