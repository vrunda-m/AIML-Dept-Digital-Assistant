class ColumnPruningAgent:
    def prune_columns(self, data, columns_to_keep):
        if not data:
            return []
        indices = [i for i, col in enumerate(data[0].keys()) if col in columns_to_keep]
        return [{col: row[col] for col in columns_to_keep} for row in data]
