export const GITHUB_URL = "https://github.com/Bancie/TiLearn";
export const PYPI_URL = "https://pypi.org/project/TiLearn/";

export type DocCard = {
  title: string;
  description: string;
  to: string;
};

export const DOC_CARDS: readonly DocCard[] = [
  {
    title: "Getting started",
    description:
      "Overview of the project, installation, and how TiLearn fits scheduling and time-management workflows.",
    to: "/getting-started",
  },
  {
    title: "User guide",
    description:
      "Problem types, algorithms (EDD, WSPT), and illustrative examples for single-machine scheduling.",
    to: "/user-guide",
  },
  {
    title: "API reference",
    description:
      "Functions, parameters, and usage for integrating TiLearn into your own Python projects.",
    to: "/api-reference",
  },
];
