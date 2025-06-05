import fx, { type DocumentData, type EnrichedResults } from "flexsearch";
import promiseOnce from "$lib/util/promise-once";

async function fetchSearchData() {
  const response = await fetch("/search-index.json");
  if (!response.ok) {
    throw new Error("Failed to fetch search index");
  }
  return response.json();
}

export const prepareSearchData = promiseOnce(async () => {
  console.log("Fetching search data...");
  const searchData = await fetchSearchData();

  const index = new fx.Document<DocType>({
    document: {
      id: "site-search",
      store: true,
      index: ["text"],
    },
  });

  for (let i = 0; i < searchData.length; i++) {
    index.add(i, searchData[i]);
  }

  return index;
});

export const searchRefs = {
  openSearch: () => {},
};

export type DocType = { routeStr: string; text: string; title: string };

export type SearchResults<D extends DocumentData = DocType> =
  EnrichedResults<D> & Array<{ doc: D }>;
