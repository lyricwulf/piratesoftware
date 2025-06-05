<script>
  import * as Table from "$lib/components/ui/table";
  const { rows = [], caption } = $$props;
</script>

<Table.Root class="kv-table">
  {#if caption}
    <Table.Caption>{caption}</Table.Caption>
  {/if}
  <!-- <Table.Header>
    <Table.Row>
      <Table.Head class="w-[100px]">Invoice</Table.Head>
      <Table.Head>Status</Table.Head>
      <Table.Head>Method</Table.Head>
      <Table.Head class="text-right">Amount</Table.Head>
    </Table.Row>
  </Table.Header> -->
  <Table.Body>
    {#each rows as row, i (i)}
      {@const key = row.key || row[0]}
      {@const value = row.value || row[1]}
      <Table.Row>
        <Table.Cell class="font-medium text-right">{key}</Table.Cell>
        <Table.Cell>{value}</Table.Cell>
      </Table.Row>
    {/each}
  </Table.Body>
</Table.Root>
