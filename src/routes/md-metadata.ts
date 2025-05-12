import DIR_METADATA from "./dir-metadata.json";

const svxFiles = import.meta.glob("/src/routes/**/*.svx", { eager: true });

export const NAV_ITEMS = { name: "", children: [], href: "" };

export const MD_METADATA = new Map<string, any>();

for (const [filePath, fileModule] of Object.entries(svxFiles)) {
  // skip annotations
  if (filePath.match(/\/annotation-\d*\.svx$/)) {
    continue;
  }
  const parts = filePath.split("/");
  const name = parts[parts.length - 2];
  const pagePath = filePath
    .replace("/src/routes", "")
    .replace("/+page.svx", "");
  const pathArr = pagePath.split("/").filter(Boolean);
  let title = fileModule.metadata.title;
  const order = fileModule.metadata.order || 0;

  MD_METADATA.set(pagePath, fileModule.metadata);

  let cur = NAV_ITEMS;
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
sortChildren(NAV_ITEMS);
