import configOptions, { init } from "@github/markdownlint-github"
const options = {
    config: init(),
    customRules: ["@github/markdownlint-github"],
    outputFormatters: [
        ["markdownlint-cli2-formatter-pretty", { "appendLink": true }] // ensures the error message includes a link to the rule documentation
    ]
}
export default options