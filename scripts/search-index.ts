import fs from "node:fs/promises";
import { convert } from "html-to-text";

const BUILD_DIR = "build";
const STATIC_DIR = "static";

async function findAllFilesWithExtension(ext: string, dir: string = BUILD_DIR) {
  const files = await fs.readdir(dir, { withFileTypes: true });
  let results: string[] = [];

  for (const file of files) {
    const res = dir + "/" + file.name;
    if (file.isDirectory()) {
      results = results.concat(await findAllFilesWithExtension(ext, res));
    } else if (file.name.endsWith(ext)) {
      results.push(res);
    }
  }
  return results;
}

async function generateSearchIndex() {
  const entries: { text: string; title: string; routeStr: string }[] = [];

  console.log(await fs.readdir(BUILD_DIR));

  const htmlFiles = await findAllFilesWithExtension(".html");

  for (const htmlFile of htmlFiles) {
    const fileContents = await fs.readFile(htmlFile, "utf-8");
    const textContent = convert(fileContents, {
      wordwrap: false,
      formatters: {
        kvFormatter: function (elem, walk, builder, formatOptions) {
          const blockFormatter = builder.options.formatters["table"];
          if (blockFormatter) {
            //  && elem.children.some(/* predicate */)
            blockFormatter(elem, walk, builder, {
              ...formatOptions,
            });
          }
        },
      },
      selectors: [
        { selector: "script", format: "skip" },
        { selector: "style", format: "skip" },
        { selector: "title", format: "skip" },
        { selector: "meta", format: "skip" },
        { selector: "nav", format: "skip" },
        { selector: ".sr-only", format: "skip" },
        ...["h1", "h2", "h3", "h4", "h5", "h6"].map((tag) => ({
          selector: tag,
          format: "heading",
          options: {
            uppercase: false,
          },
        })),
        { selector: ".markdown", format: "inline" },
        { selector: ".kv-table", format: "kvFormatter" },
      ],
    });

    let routeStr = htmlFile.replace(BUILD_DIR, "");

    if (!routeStr.startsWith("/archive")) {
      routeStr = routeStr.replace(".html", "");
    }

    let title = fileContents.match(/<title>(.*?)<\/title>/)?.[1] || routeStr;

    if (title === "Exported Data") {
      title = routeStr;
    }

    entries.push({
      text: textContent,
      title,
      routeStr,
    });
  }

  fs.writeFile(
    `${BUILD_DIR}/search-index.json`,
    JSON.stringify(entries, null, 2)
  );
  fs.writeFile(
    `${STATIC_DIR}/search-index.json`,
    JSON.stringify(entries, null, 2)
  );
}

generateSearchIndex();
