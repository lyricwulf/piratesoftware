<script>
  import * as Table from "$lib/components/ui/table";
  import { ScrollArea } from "$lib/components/ui/scroll-area";
  const { csv = "", caption, headers: useHeaders = true } = $props();

  const rows = csv.split(/[\r\n]+/).map((line) => {
    const regex = /\s*("[^"]*"|[^,]*)\s*/;
    return line
      .split(regex)
      .filter((cell) => cell && cell !== ",")
      .map((cell) => {
        // Remove surrounding quotes if present
        return cell.startsWith('"') && cell.endsWith('"')
          ? cell.slice(1, -1)
          : cell;
      });
  });
  const headers = useHeaders && rows.shift();
  console.log("Headers:", headers);
  console.log("Rows:", rows);
</script>

<ScrollArea
  class="h-[40vh] rounded-md border relative"
  scrollbarYClasses="z-10"
>
  <Table.Root>
    {#if caption}
      <Table.Caption>{caption}</Table.Caption>
    {/if}
    <Table.Header
      class="sticky top-0 z-10 bg-background"
      style="box-shadow: inset 0 -2px 0 hsl(var(--border));"
    >
      <Table.Row>
        {#if headers}
          {#each headers as header, n}
            <Table.Head data-header-n={n}>{header}</Table.Head>
          {/each}
        {/if}
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {#each rows as row, i (i)}
        <Table.Row>
          {#each row as cell, n}
            <Table.Cell data-cell-n={n}>{cell}</Table.Cell>
          {/each}
        </Table.Row>
      {/each}
    </Table.Body>
  </Table.Root>
</ScrollArea>
