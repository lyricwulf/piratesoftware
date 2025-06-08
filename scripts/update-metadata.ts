import DIR_METADATA from "./dir-metadata.json";
import fs from "node:fs/promises";
import { compile } from "mdsvex";

const OUTPUT_DIR = "src/lib/__derived";

function get_headings() {
  let visit;
  let tree_to_string;
  let GithubSlugger;
  return async function transformer(tree, vFile) {
    if (!visit || !GithubSlugger) {
      tree_to_string = (await import("mdast-util-to-string")).toString;
      visit = (await import("unist-util-visit")).visit;
      GithubSlugger = (await import("github-slugger")).default;
    }

    const slugger = new GithubSlugger();

    const headings = [];

    visit(tree, "heading", (node) => {
      const title = tree_to_string(node);
      headings.push({
        level: node.depth,
        title,
        slug: slugger.slug(title),
      });
    });

    vFile.data.fm ||= {};
    vFile.data.fm.headings = headings;
  };
}

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

async function generateMetadata() {
  const svxFiles = await findAllFilesWithExtension("+page.svx", "src/routes");

  const navItems = { name: "", children: [], href: "" };

  const mdMetadata: Record<string, any> = {};

  for (const filePath of svxFiles) {
    const fileContents = await fs.readFile(filePath, "utf-8");
    const fileSvx = await compile(fileContents, {
      remarkPlugins: [get_headings],
    });
    const fileModule = {
      metadata: fileSvx?.data.fm,
    };
    const parts = filePath.split("/");
    const name = parts[parts.length - 2];
    const pagePath = filePath
      .replace("src/routes", "")
      .replace("/+page.svx", "");
    const pathArr = pagePath.split("/").filter(Boolean);
    let title = fileModule.metadata.title;
    const order = fileModule.metadata.order || 0;

    mdMetadata[pagePath] = fileModule.metadata;

    let cur = navItems;
    for (const part of pathArr) {
      let found = cur.children.find((child) => child.code === part);

      if (!found) {
        found = { code: part, name: part, children: [], href: "" };
        if (DIR_METADATA[part]) {
          found.name = DIR_METADATA[part].name;
          found.order = DIR_METADATA[part].order;
        }

        cur.children.push(found);
      }

      cur = found;
    }

    cur.name = title;
    cur.href = pagePath;
    cur.order = order;
  }

  // recursively sort the children of each item
  const sortChildren = (item: any) => {
    item.children.sort((a: any, b: any) => a.order - b.order);
    for (const child of item.children) {
      sortChildren(child);
    }
  };
  sortChildren(navItems);
  return { navItems, mdMetadata };
}

export async function updateMetadata() {
  const { navItems, mdMetadata } = await generateMetadata();
  const outputPath = `${OUTPUT_DIR}/metadata.json`;
  await fs.mkdir(OUTPUT_DIR, { recursive: true });
  await fs.writeFile(outputPath, JSON.stringify({ navItems, mdMetadata }));
}

updateMetadata();
