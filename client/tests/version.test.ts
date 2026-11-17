import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

import { expect, test } from "vitest";

import { VERSION } from "../src/version.js";

const here = dirname(fileURLToPath(import.meta.url));
const packageJson = JSON.parse(readFileSync(resolve(here, "../package.json"), "utf8")) as {
  version: string;
};

test("client version matches the package version", () => {
  expect(VERSION).toBe(packageJson.version);
});
