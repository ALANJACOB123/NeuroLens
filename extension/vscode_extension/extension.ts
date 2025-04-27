// VS Code Extension for inline code completions

import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    const provider = vscode.languages.registerInlineCompletionItemProvider('*', {
        provideInlineCompletionItems(document, position) {
            const suggestion = new vscode.InlineCompletionItem('// suggestion based on EEG state');
            return [suggestion];
        }
    });
    context.subscriptions.push(provider);
}

export function deactivate() {}
