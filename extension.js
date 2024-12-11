const vscode = require('vscode');
const { execSync } = require('child_process');
const path = require('path');

function activate(context) {
  let disposable = vscode.commands.registerCommand('extension.checkNPlusOne', async function () {
    const workspaceFolders = vscode.workspace.workspaceFolders;

    if (!workspaceFolders) {
      vscode.window.showErrorMessage("No workspace folder found.");
      return;
    }

    const workspacePath = workspaceFolders[0].uri.fsPath;
    const scriptPath = path.resolve(__dirname, './n1_detector.py');

    try {
      // Run the Python script to detect N+1 problems
      const result = execSync(`python3 ${scriptPath}`, { encoding: 'utf8' });
      vscode.window.showInformationMessage("N+1 Detection Results:\n" + result);
    } catch (error) {
      vscode.window.showErrorMessage("Failed to detect N+1 problems. Error: " + error.message);
    }
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
